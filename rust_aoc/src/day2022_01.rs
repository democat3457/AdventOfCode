use std::fmt::Display;

pub fn solve_p1(input: String) -> impl Display {
    for i in &input.split('\n').collect::<Vec<_>>()[..10] {
        println!("Debug: {i}\t{}", i.len());
    }
    0
}
