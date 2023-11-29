import React, { useState, useEffect } from 'react';
import LoginPage from './LoginPage';
import Home from './Home';
import News from './News';
import Profile from './Profile';
import Navbar from './Navbar';

const Content = () => {
  const [authenticated, setAuthenticated] = useState(localStorage.getItem('authenticated') === 'true');
  const [currentRoute, setCurrentRoute] = useState(window.location.pathname);

  const handleLogin = (username, password) => {
    if (username === 'Admin' && password === '12345') {
      setAuthenticated(true);
      localStorage.setItem('authenticated', 'true');
      setCurrentRoute('/profile');
    } else {
      alert('Incorrect username or password.');
    }
  };

  const handleLogout = () => {
    setAuthenticated(false);
    localStorage.setItem('authenticated', 'false');
    setCurrentRoute('/');
  };

  const routes = {
    '/': <Home />,
    '/news': <News />,
    '/profile': <Profile authenticated={authenticated} />,
    '/login': !authenticated && <LoginPage onLogin={handleLogin} />,
  };

  const updateContent = () => {
    setCurrentRoute(window.location.pathname);
  };

  useEffect(() => {
    window.addEventListener('popstate', updateContent);

    return () => {
      window.removeEventListener('popstate', updateContent);
    };
  }, []);

  useEffect(() => {
    const event = new Event('loginStateChanged');
    window.dispatchEvent(event);
  }, [authenticated]);

  const ContentComponent = routes[currentRoute] || routes['/'];

  return (
    <div>
      <Navbar authenticated={authenticated} onLogout={handleLogout} />
      {ContentComponent}
    </div>
  );
};

export default Content;
