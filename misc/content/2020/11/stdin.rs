fn main() {
    let mut buffer = String::from("initial content");
    let stdin = std::io::stdin(); // We get `Stdin` here.
    let s = stdin.read_line(&mut buffer);
    println!("Buffer: {}", buffer);
    println!("{:?}", s);
}
