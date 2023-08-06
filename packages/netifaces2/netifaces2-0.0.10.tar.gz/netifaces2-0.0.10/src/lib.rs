use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

mod linux;
mod types;

#[pyfunction]
fn rs_interfaces() -> PyResult<Vec<String>> {
    let maybe_ifs = linux::linux_interfaces();

    maybe_ifs.map_err(|e| {
        let str_message = e.to_string();
        PyErr::new::<PyRuntimeError, _>(str_message)
    })
}

#[pyfunction]
fn rs_ifaddresses(if_name: &str) -> PyResult<types::IfAddrs> {
    let maybe_ifaddrs = linux::linux_ifaddresses(if_name);

    maybe_ifaddrs.map_err(|e| {
        let str_message = e.to_string();
        PyErr::new::<PyRuntimeError, _>(str_message)
    })
}

#[pymodule]
fn netifaces(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rs_interfaces, m)?)?;
    m.add_function(wrap_pyfunction!(rs_ifaddresses, m)?)?;
    Ok(())
}
