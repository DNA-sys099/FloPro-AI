import React, { useState } from 'react';
import './ContentStudio.css';

const ContentStudio = () => {
  const [selectedPlatforms, setSelectedPlatforms] = useState([]);
  const [contentType, setContentType] = useState(null);
  
  return (
    <div className="content-studio">
      <div className="studio-header">
        <h2>Content Studio</h2>
        <div className="header-actions">
          <button className="save-draft">Save Draft</button>
          <button className="publish">Publish</button>
        </div>
      </div>

      <div className="studio-grid">
        {/* Content Creation Area */}
        <div className="creation-area">
          <div className="platform-selector">
            <h3>Platforms</h3>
            <div className="platform-buttons">
              <button 
                className={`platform-btn ${selectedPlatforms.includes('facebook') ? 'active' : ''}`}
                onClick={() => setSelectedPlatforms([...selectedPlatforms, 'facebook'])}
              >
                <i className="ri-facebook-fill"></i>
                Facebook
              </button>
              <button 
                className={`platform-btn ${selectedPlatforms.includes('instagram') ? 'active' : ''}`}
                onClick={() => setSelectedPlatforms([...selectedPlatforms, 'instagram'])}
              >
                <i className="ri-instagram-line"></i>
                Instagram
              </button>
              <button 
                className={`platform-btn ${selectedPlatforms.includes('linkedin') ? 'active' : ''}`}
                onClick={() => setSelectedPlatforms([...selectedPlatforms, 'linkedin'])}
              >
                <i className="ri-linkedin-fill"></i>
                LinkedIn
              </button>
            </div>
          </div>

          <div className="content-type-selector">
            <h3>Content Type</h3>
            <div className="type-buttons">
              <button 
                className={`type-btn ${contentType === 'product' ? 'active' : ''}`}
                onClick={() => setContentType('product')}
              >
                <i className="ri-shopping-bag-line"></i>
                Product
              </button>
              <button 
                className={`type-btn ${contentType === 'update' ? 'active' : ''}`}
                onClick={() => setContentType('update')}
              >
                <i className="ri-newspaper-line"></i>
                Company Update
              </button>
              <button 
                className={`type-btn ${contentType === 'event' ? 'active' : ''}`}
                onClick={() => setContentType('event')}
              >
                <i className="ri-calendar-event-line"></i>
                Event
              </button>
            </div>
          </div>

          <div className="content-editor">
            <div className="editor-header">
              <h3>Content</h3>
              <button className="ai-assist">
                <i className="ri-magic-line"></i>
                AI Assist
              </button>
            </div>
            
            <div className="media-uploader">
              <div className="upload-area">
                <i className="ri-upload-cloud-line"></i>
                <span>Drag and drop media here or click to upload</span>
                <span className="file-types">Supports: JPG, PNG, MP4, GIF</span>
              </div>
            </div>

            <div className="text-editor">
              <textarea 
                placeholder="Write your post content here..."
                className="content-textarea"
              ></textarea>
              
              <div className="editor-tools">
                <button><i className="ri-emotion-line"></i></button>
                <button><i className="ri-link"></i></button>
                <button><i className="ri-hashtag"></i></button>
                <button><i className="ri-at-line"></i></button>
              </div>
            </div>
          </div>
        </div>

        {/* Preview & Analytics Area */}
        <div className="preview-area">
          <div className="preview-header">
            <h3>Preview</h3>
            <div className="preview-controls">
              <button className="preview-platform">
                <i className="ri-facebook-fill"></i>
              </button>
              <button className="preview-platform">
                <i className="ri-instagram-line"></i>
              </button>
              <button className="preview-platform">
                <i className="ri-linkedin-fill"></i>
              </button>
            </div>
          </div>

          <div className="preview-frame">
            {/* Dynamic preview content */}
          </div>

          <div className="performance-prediction">
            <h3>AI Performance Prediction</h3>
            <div className="prediction-metrics">
              <div className="metric">
                <span className="metric-label">Estimated Reach</span>
                <span className="metric-value">15K - 20K</span>
              </div>
              <div className="metric">
                <span className="metric-label">Engagement Rate</span>
                <span className="metric-value">4.2%</span>
              </div>
              <div className="metric">
                <span className="metric-label">Best Time to Post</span>
                <span className="metric-value">3:00 PM Today</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Scheduling Options */}
      <div className="scheduling-options">
        <h3>Schedule</h3>
        <div className="schedule-buttons">
          <button className="schedule-btn">
            <i className="ri-time-line"></i>
            Post Now
          </button>
          <button className="schedule-btn">
            <i className="ri-calendar-line"></i>
            Schedule
          </button>
          <button className="schedule-btn">
            <i className="ri-magic-line"></i>
            Best Time (AI)
          </button>
        </div>
      </div>
    </div>
  );
};

export default ContentStudio;
