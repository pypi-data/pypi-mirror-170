use crate::box_def::Box;
use crate::interval_tree::{Interval, IntervalTree};
use adjacent_pair_iterator::AdjacentPairIterator;
use std::cmp::{max, min};

#[derive(Clone, Copy)]
struct CalcBox {
    x1: i32,
    y1: i32,
    x2: i32,
    y2: i32,
}
fn to_calc_box(b: &Box) -> CalcBox {
    CalcBox {
        x1: b.x1,
        x2: b.x1 + b.xs as i32,
        y1: b.y1,
        y2: b.y1 + b.ys as i32,
    }
}
fn to_box(b: &CalcBox) -> Box {
    Box {
        x1: b.x1,
        xs: (b.x2 - b.x1) as u32,
        y1: b.y1,
        ys: (b.y2 - b.y1) as u32,
    }
}
const MIN_BIN_SIZE: usize = 8;
fn does_intersect(b1: &CalcBox, b2: &CalcBox) -> bool {
    b1.y2 > b2.y1 && b1.y1 < b2.y2 && b1.x2 > b2.x1 && b1.x1 < b2.x2
}
// Flipper is a type-level utility for recursive box flipping for compile-time box flipping
trait SortAxis {
    type Transpose: SortAxis;
    fn left(b: &CalcBox) -> i32;
    fn right(b: &CalcBox) -> i32;
}
struct YAxis {}
struct XAxis {}
impl SortAxis for YAxis {
    type Transpose = XAxis;
    fn left(b: &CalcBox) -> i32 {
        b.y1
    }
    fn right(b: &CalcBox) -> i32 {
        b.y2
    }
}
impl SortAxis for XAxis {
    type Transpose = YAxis;
    fn left(b: &CalcBox) -> i32 {
        b.x1
    }
    fn right(b: &CalcBox) -> i32 {
        b.x2
    }
}
pub struct RTSNode {
    left: i32,
    right: i32,
    children: Option<IntervalTree<i32, RTSNode>>,
    data: Vec<(CalcBox, u32)>,
}
impl RTSNode {
    pub fn new(boxes: &[Box]) -> RTSNode {
        assert!(!boxes.is_empty(), "Must have more than 0 boxes");
        assert!(
            (boxes.len() as u64) < ((1_u64) << 32),
            "Only supports 4 billion boxes"
        );
        RTSNode::build_node::<XAxis>(
            boxes
                .iter()
                .enumerate()
                .map(|(idx, b)| (to_calc_box(b), idx as u32))
                .collect(),
        )
    }
    fn build_node<Axis: SortAxis>(mut boxes: Vec<(CalcBox, u32)>) -> RTSNode {
        let (parent_left, parent_right) =
            boxes
                .iter()
                .fold((std::i32::MAX, std::i32::MIN), |(left, right), (b, _)| {
                    (
                        min(Axis::Transpose::left(b), left),
                        max(Axis::Transpose::right(b), right),
                    )
                });
        // if data is small, brute force search is fastest, don't continue splitting, just optimize in place
        if boxes.len() <= MIN_BIN_SIZE {
            RTSNode {
                left: parent_left,
                right: parent_right,
                children: None,
                data: boxes,
            }
        } else {
            // self.data is assumed to be sorted by x1
            boxes.sort_unstable_by_key(|(b, _)| Axis::left(b));

            // A greedy method to find the optimal splitting points in the sorted data.
            // It defines a splitting point as "locally optimal" where there are 2x as many objects fully inside
            // the split as across the split.
            let mut rights: Vec<i32> = boxes.iter().map(|(b, _)| Axis::right(b)).collect();
            rights.sort_unstable();

            let mut left_idxs: Vec<usize> = vec![0];
            let mut inner_count = 0;
            let mut past_count = 0;
            let mut x2idx = 0;
            for (idx, (orig_b, _)) in boxes.iter().enumerate() {
                inner_count += 1;
                while Axis::left(orig_b) > rights[x2idx] {
                    inner_count -= 1;
                    past_count += 1;
                    x2idx += 1;
                }
                if past_count > 2 * inner_count && past_count > MIN_BIN_SIZE {
                    past_count = 0;
                    left_idxs.push(idx);
                }
            }
            // remove the last division, as there is no provable benefit to keeping it around
            // as we don't know how big the number of unique values in the 2nd sector is a-priori
            left_idxs.pop();
            // complete the last sector
            left_idxs.push(boxes.len());
            //if there aren't at least 2 new sectors, then just create a basic node
            if left_idxs.len() < 3 {
                RTSNode {
                    left: parent_left,
                    right: parent_right,
                    children: None,
                    data: boxes,
                }
            } else {
                let child_iter = left_idxs.adjacent_pairs().map(|(lidx, ridx)| {
                    let child_boxes = boxes[lidx..ridx].to_vec();
                    RTSNode::build_node::<Axis::Transpose>(child_boxes)
                });
                let children = Some(IntervalTree::create_from_fn(child_iter, |n| Interval {
                    left: n.left,
                    right: n.right,
                }));
                RTSNode {
                    left: parent_left,
                    right: parent_right,
                    children: children,
                    data: Vec::new(), //no data of its own
                }
            }
        }
    }
    fn search_visitor_cb<F, Axis>(&self, orig_b1: &CalcBox, vistor: &mut F)
    where
        F: FnMut(&u32, &Box),
        Axis: SortAxis,
    {
        match &self.children {
            None => {
                for (b2, idx) in self.data.iter() {
                    if does_intersect(orig_b1, b2) {
                        vistor(idx, &to_box(b2));
                    }
                }
            }
            Some(tree) => {
                tree.find_overlaps_visitor(
                    &Interval {
                        left: Axis::left(orig_b1),
                        right: Axis::right(orig_b1),
                    },
                    &mut |item| {
                        item.search_visitor_cb::<F, Axis::Transpose>(orig_b1, vistor);
                    },
                );
            }
        }
    }
    pub fn search_visitor<F>(&self, b1: &Box, vistor: &mut F)
    where
        F: FnMut(&u32, &Box),
    {
        self.search_visitor_cb::<F, XAxis>(&to_calc_box(b1), vistor);
    }
    pub fn find_intersections(&self, b1: &Box) -> Vec<u32> {
        let mut v: Vec<u32> = Vec::new();
        self.search_visitor(b1, &mut |idx, _| {
            v.push(*idx);
        });
        v
    }
}
/*
Tested in find_intersecting_asym, find_intersecting
*/
