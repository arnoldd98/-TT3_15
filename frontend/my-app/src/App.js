import logo from "./logo.svg";
import "./bootstrap.min.css";
import "./App.css";
import HomePage from "./components/HomePage";
import Login from "./components/Login";
import { Outlet, Link } from "react-router-dom";

function App() {
  const isAuthenticated = true;
  return (
    <>
      <Login isAuthenticated={isAuthenticated} />
      <Link to="/HomePage">Homepage</Link>
      <Outlet />
    </>
  );
}

export default App;
