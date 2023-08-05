use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn evatools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<MeanCaculator>()?;
    Ok(())
}

#[pyclass]
#[pyo3(text_signature = "($self)")]
struct MeanCaculator {
    val: f64,
    total: f64,
}

#[pymethods]
impl MeanCaculator {
    #[new]
    fn new() -> Self {
        Self {
            val: 0.0,
            total: 0.0,
        }
    }

    #[pyo3(text_signature = "($self, item)")]
    fn add(&mut self, item: f64) {
        self.val += item;
        self.total += 1.0;
    }

    #[getter(result)]
    fn get_result(&self) -> f64 {
        self.val / self.total
    }

    #[pyo3(text_signature = "($self)")]
    fn reset(&mut self) -> f64 {
        let rlt = self.get_result();
        self.val = 0.0;
        self.total = 0.0;
        rlt
    }

    #[getter]
    fn get_val(&self) -> f64 {
        self.val
    }

    #[getter]
    fn get_total(&self) -> f64 {
        self.total
    }
}
