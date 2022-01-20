import logo from "./logo.svg";
import "./bootstrap.min.css";
import "./App.css";
import HomePage from "./components/HomePage";
import Login from "./components/Login";
import { Outlet, Link } from "react-router-dom";

function App() {
  return (
    <>
      <div>Hello</div>
      <Link to="/HomePage">HomePage</Link>
      <Outlet />
    </>
  );
}

export default App;
