import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <div>Home Page.</div>;
}

function About() {
  return <div>About Page.</div>;
}

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;