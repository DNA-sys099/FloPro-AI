import React, { useState } from 'react';
import './EasyPostCreator.css';

const EasyPostCreator = () => {
  const [step, setStep] = useState(1);
  
  return (
    <div className="easy-post-creator">
      {/* Step 1: Choose Post Type */}
      {step === 1 && (
        <div className="post-type-selector">
          <h1>What would you like to share?</h1>
          
          <div className="big-button-grid">
            <button onClick={() => setStep(2)} className="big-button product">
              <img src="/icons/product.svg" alt="Product" />
              <span>Product</span>
            </button>
            
            <button onClick={() => setStep(2)} className="big-button service">
              <img src="/icons/service.svg" alt="Service" />
              <span>Service</span>
            </button>
            
            <button onClick={() => setStep(2)} className="big-button update">
              <img src="/icons/news.svg" alt="Company Update" />
              <span>Company Update</span>
            </button>
            
            <button onClick={() => setStep(2)} className="big-button tips">
              <img src="/icons/tips.svg" alt="Tips" />
              <span>Tips & Advice</span>
            </button>
          </div>
        </div>
      )}
      
      {/* Step 2: Add Content */}
      {step === 2 && (
        <div className="content-creator">
          <h1>Add Your Content</h1>
          
          <div className="content-options">
            <div className="upload-section">
              <button className="upload-button">
                <img src="/icons/image.svg" alt="Upload" />
                <span>Add Photo or Video</span>
              </button>
            </div>
            
            <div className="text-section">
              <button className="ai-helper">
                <img src="/icons/magic.svg" alt="AI Help" />
                <span>Help Me Write This</span>
              </button>
              
              <textarea 
                placeholder="What would you like to say? Type here or click 'Help Me Write This'"
                className="big-text-input"
              />
            </div>
          </div>
          
          <div className="navigation-buttons">
            <button onClick={() => setStep(1)} className="back-button">
              <img src="/icons/back.svg" alt="Back" />
              <span>Back</span>
            </button>
            
            <button onClick={() => setStep(3)} className="next-button">
              <span>Next</span>
              <img src="/icons/next.svg" alt="Next" />
            </button>
          </div>
        </div>
      )}
      
      {/* Step 3: Choose When to Post */}
      {step === 3 && (
        <div className="schedule-picker">
          <h1>When should we post this?</h1>
          
          <div className="timing-options">
            <button className="timing-button">
              <img src="/icons/now.svg" alt="Post Now" />
              <span>Post Now</span>
            </button>
            
            <button className="timing-button">
              <img src="/icons/best-time.svg" alt="Best Time" />
              <span>Best Time (AI Recommended)</span>
            </button>
            
            <button className="timing-button">
              <img src="/icons/calendar.svg" alt="Pick Time" />
              <span>Pick a Time</span>
            </button>
          </div>
          
          <div className="navigation-buttons">
            <button onClick={() => setStep(2)} className="back-button">
              <img src="/icons/back.svg" alt="Back" />
              <span>Back</span>
            </button>
            
            <button className="finish-button">
              <span>Finish</span>
              <img src="/icons/check.svg" alt="Finish" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default EasyPostCreator;
