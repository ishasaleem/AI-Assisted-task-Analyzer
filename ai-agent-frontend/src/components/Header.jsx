import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="bg-gradient-to-r from-purple-500 to-pink-500 p-4 text-white flex justify-between">
      <h1 className="font-bold text-xl">AI Agent Task Analyzer</h1>
      <nav>
        <Link to="/" className="mr-4 hover:underline">Home</Link>
        <Link to="/about" className="hover:underline">About</Link>
      </nav>
    </header>
  );
}
