import React, { useState } from 'react';
import './SignupForm.css';

const SignupForm = () => {
  const [formData, setFormData] = useState({
    businessName: '',
    businessType: 'retail',
    email: '',
    website: '',
    targetAudience: '',
    mainGoals: [],
    socialPlatforms: [],
    currentChallenges: ''
  });

  const businessTypes = [
    { value: 'retail', label: 'Retail Store' },
    { value: 'restaurant', label: 'Restaurant/Café' },
    { value: 'fitness', label: 'Fitness/Gym' },
    { value: 'salon', label: 'Beauty Salon/Spa' },
    { value: 'real_estate', label: 'Real Estate' },
    { value: 'other', label: 'Other' }
  ];

  const goals = [
    'Increase brand awareness',
    'Drive more sales',
    'Improve customer engagement',
    'Generate leads',
    'Build community',
    'Showcase products/services'
  ];

  const platforms = [
    'Instagram',
    'Facebook',
    'Twitter',
    'LinkedIn',
    'TikTok',
    'YouTube'
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleCheckboxChange = (e, category) => {
    const { value, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [category]: checked 
        ? [...prev[category], value]
        : prev[category].filter(item => item !== value)
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        const data = await response.json();
        // Handle success (e.g., show success message, redirect)
      }
    } catch (error) {
      // Handle error
    }
  };

  return (
    <div className="signup-container">
      <div className="signup-content">
        <h1>Get Your Custom Business Growth Guide</h1>
        <p className="subtitle">Tell us about your business to receive a personalized strategy guide</p>

        <form onSubmit={handleSubmit} className="signup-form">
          <div className="form-section">
            <h2>Business Information</h2>
            
            <div className="form-group">
              <label htmlFor="businessName">Business Name</label>
              <input
                type="text"
                id="businessName"
                name="businessName"
                value={formData.businessName}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="businessType">Business Type</label>
              <select
                id="businessType"
                name="businessType"
                value={formData.businessType}
                onChange={handleChange}
                required
              >
                {businessTypes.map(type => (
                  <option key={type.value} value={type.value}>
                    {type.label}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="email">Business Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="website">Website (Optional)</label>
              <input
                type="url"
                id="website"
                name="website"
                value={formData.website}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="form-section">
            <h2>Target Audience</h2>
            
            <div className="form-group">
              <label htmlFor="targetAudience">Describe your ideal customer</label>
              <textarea
                id="targetAudience"
                name="targetAudience"
                value={formData.targetAudience}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-section">
            <h2>Business Goals</h2>
            
            <div className="checkbox-group">
              {goals.map(goal => (
                <label key={goal} className="checkbox-label">
                  <input
                    type="checkbox"
                    value={goal}
                    checked={formData.mainGoals.includes(goal)}
                    onChange={(e) => handleCheckboxChange(e, 'mainGoals')}
                  />
                  {goal}
                </label>
              ))}
            </div>
          </div>

          <div className="form-section">
            <h2>Social Media Platforms</h2>
            
            <div className="checkbox-group">
              {platforms.map(platform => (
                <label key={platform} className="checkbox-label">
                  <input
                    type="checkbox"
                    value={platform}
                    checked={formData.socialPlatforms.includes(platform)}
                    onChange={(e) => handleCheckboxChange(e, 'socialPlatforms')}
                  />
                  {platform}
                </label>
              ))}
            </div>
          </div>

          <div className="form-section">
            <h2>Current Challenges</h2>
            
            <div className="form-group">
              <label htmlFor="currentChallenges">What are your biggest social media challenges?</label>
              <textarea
                id="currentChallenges"
                name="currentChallenges"
                value={formData.currentChallenges}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <button type="submit" className="submit-button">
            Get Your Custom Guide
          </button>
        </form>
      </div>
    </div>
  );
};

export default SignupForm;
