import { useLocation, Link } from "react-router-dom";

export default function Success() {
  const location = useLocation();
  const user = location.state?.user || "User";

  return (
    <div>
      <h1>Login Successful</h1>
      <p>Welcome, {user}!</p>
      <Link to="/">Go back to Home</Link>
    </div>
  );
}
