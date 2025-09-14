import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div>
      <h1>Welcome to WithMe App</h1>
      <p>Please choose an option:</p>
      <Link to="/register"><button>Register</button></Link>
      <Link to="/login"><button>Login</button></Link>
    </div>
  );
}
