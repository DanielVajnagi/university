import React from 'react';

const Navbar = ({ authenticated, onLogout }) => {
  return (
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/news">News</a></li>
        <li><a href="/profile">Profile</a></li>
        {!authenticated && <li><button className="login-button"><a href="/login">Login</a></button></li>}
        {authenticated && <li><button className="logout-button" onClick={onLogout}>Logout</button></li>}
      </ul>
    </nav>
  );
};

export default Navbar;
