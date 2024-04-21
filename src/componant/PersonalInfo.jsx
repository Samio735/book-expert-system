import React from 'react'
import "./PersonalInfo.css"
import profileImg from '../scenes/images/img.png';
import notificationIcon from '../scenes/images/icons8-bell-100 1.png';

export default function PersonalInfo() {
  return (
    
    <div className="profile-container">
        <img src={profileImg} alt="Profile" />
        <h3>Wail Hamlaoui</h3>
        <div className="notification-icon-container">
          <img src={notificationIcon} alt="Notification" />
        </div>
    </div>

  )
}
