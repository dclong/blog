use log;
use simple_logger::SimpleLogger;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ParseRankError {
    #[error("{0} is not a valid symbol for card rank!")]
    InvalidSymbol(char),
    #[error("{0} is not a valid integer for card rank!")]
    InvalidInteger(u8),
}

fn main() {
    SimpleLogger::new().init().unwrap();
    log::warn!("This is an example message.");
    log::error!("{}", ParseRankError::InvalidSymbol('m'));
}
