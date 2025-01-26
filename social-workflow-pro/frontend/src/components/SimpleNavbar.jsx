import React from 'react';
import './SimpleNavbar.css';

const SimpleNavbar = () => {
  return (
    <nav className="simple-navbar">
      <div className="nav-item home">
        <img src="/icons/home.svg" alt="Home" />
        <span>Home</span>
      </div>
      
      <div className="nav-item create">
        <img src="/icons/create.svg" alt="Create Post" />
        <span>Create Post</span>
      </div>
      
      <div className="nav-item calendar">
        <img src="/icons/calendar.svg" alt="Calendar" />
        <span>Schedule</span>
      </div>
      
      <div className="nav-item results">
        <img src="/icons/chart.svg" alt="Results" />
        <span>Results</span>
      </div>
      
      <div className="nav-item help">
        <img src="/icons/help.svg" alt="Help" />
        <span>Help</span>
      </div>
    </nav>
  );
};

export default SimpleNavbar;
