import React from 'react';
import './ModernDashboard.css';

const ModernDashboard = () => {
  return (
    <div className="dashboard-container">
      {/* Sleek Side Navigation */}
      <nav className="side-nav">
        <div className="company-logo">
          <img src="/logo.svg" alt="Social Workflow Pro" />
        </div>
        
        <div className="nav-sections">
          <div className="nav-item active">
            <i className="ri-dashboard-line"></i>
            <span>Dashboard</span>
          </div>
          
          <div className="nav-item">
            <i className="ri-add-circle-line"></i>
            <span>Create Content</span>
          </div>
          
          <div className="nav-item">
            <i className="ri-calendar-line"></i>
            <span>Content Calendar</span>
          </div>
          
          <div className="nav-item">
            <i className="ri-bar-chart-line"></i>
            <span>Analytics</span>
          </div>
          
          <div className="nav-item">
            <i className="ri-customer-service-2-line"></i>
            <span>AI Assistant</span>
          </div>
        </div>
      </nav>

      {/* Main Content Area */}
      <main className="main-content">
        {/* Top Bar */}
        <div className="top-bar">
          <div className="search-bar">
            <i className="ri-search-line"></i>
            <input type="text" placeholder="Search content, campaigns, analytics..." />
          </div>
          
          <div className="quick-actions">
            <button className="action-btn">
              <i className="ri-add-line"></i>
              Quick Post
            </button>
            
            <button className="action-btn">
              <i className="ri-calendar-check-line"></i>
              Schedule
            </button>
          </div>
        </div>

        {/* Content Overview */}
        <div className="content-grid">
          <div className="metric-card">
            <div className="metric-header">
              <h3>Content Performance</h3>
              <span className="period">Last 30 Days</span>
            </div>
            <div className="metric-content">
              <div className="metric-value">
                <span className="number">89%</span>
                <span className="label">Engagement Rate</span>
              </div>
              <div className="metric-chart">
                {/* Chart Component */}
              </div>
            </div>
          </div>

          <div className="metric-card">
            <div className="metric-header">
              <h3>Scheduled Content</h3>
              <span className="period">Next 7 Days</span>
            </div>
            <div className="content-schedule">
              <div className="schedule-item">
                <div className="time">Today, 3:00 PM</div>
                <div className="content-type">Product Update</div>
                <div className="platforms">
                  <i className="ri-facebook-fill"></i>
                  <i className="ri-instagram-line"></i>
                </div>
              </div>
              {/* More schedule items */}
            </div>
          </div>

          <div className="metric-card">
            <div className="metric-header">
              <h3>AI Insights</h3>
              <span className="period">Real-time</span>
            </div>
            <div className="insights-list">
              <div className="insight-item">
                <i className="ri-lightbulb-line"></i>
                <span>Best time to post today: 3:00 PM</span>
              </div>
              <div className="insight-item">
                <i className="ri-line-chart-line"></i>
                <span>Trending topic in your industry: Innovation</span>
              </div>
            </div>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="recent-activity">
          <h3>Recent Activity</h3>
          <div className="activity-list">
            <div className="activity-item">
              <div className="activity-icon success">
                <i className="ri-check-line"></i>
              </div>
              <div className="activity-details">
                <span className="activity-title">Product Launch Post Published</span>
                <span className="activity-time">2 hours ago</span>
              </div>
              <div className="activity-metrics">
                <span className="metric">
                  <i className="ri-heart-line"></i>
                  234
                </span>
                <span className="metric">
                  <i className="ri-share-forward-line"></i>
                  45
                </span>
              </div>
            </div>
            {/* More activity items */}
          </div>
        </div>
      </main>

      {/* Right Sidebar */}
      <aside className="right-sidebar">
        <div className="sidebar-section">
          <h3>Quick Analytics</h3>
          <div className="analytics-summary">
            <div className="summary-item">
              <span className="label">Total Reach</span>
              <span className="value">45.2K</span>
              <span className="change positive">+12.5%</span>
            </div>
            {/* More summary items */}
          </div>
        </div>

        <div className="sidebar-section">
          <h3>Content Queue</h3>
          <div className="queue-list">
            {/* Queue items */}
          </div>
        </div>
      </aside>
    </div>
  );
};

export default ModernDashboard;
