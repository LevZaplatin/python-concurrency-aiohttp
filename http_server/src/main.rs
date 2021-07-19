#[macro_use] extern crate rocket;

use std::thread;
use std::time::Duration;

#[get("/")]
fn index() -> &'static str {
    thread::sleep(Duration::from_secs(1));
    "Hello, world!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}