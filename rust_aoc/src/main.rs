use std::io;
use std::io::prelude::*;
use std::fs::File;

mod day2022_01;

fn fetch_input(day: &i32) -> io::Result<String> {
    let mut f = File::open(format!("../inputs/2022_{day:02}.txt"))?;
    let mut buf = String::new();

    f.read_to_string(&mut buf)?;
    Ok(buf)
}

fn main() -> io::Result<()> {
    let input = fetch_input(&1)?;

    let result = day2022_01::solve_p1(input);
    println!("\nPart 1: {result}");
    Ok(())
}
