import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Home from "./Pages/Home";
import Login from "./Pages/Login";
import Dashboard from "./Pages/Dashboard";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const handleLogout = () => {
    setLoggedIn(false);
  };

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (token) {
      setLoggedIn(true); // optionally validate later via API
    }
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        
        <Route
          path="/login"
          element={
            loggedIn ? (
              <Navigate to="/dashboard" />
            ) : (
              <Login onLogin={() => setLoggedIn(true)} />
            )
          }
        />

         <Route
          path="/dashboard"
          element={
            loggedIn ? (
              <Dashboard onLogout={handleLogout} />
            ) : (
              <Navigate to="/login" />
            )
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
