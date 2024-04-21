import React from 'react'
import "./team.css"
import image from "../images/img.png"

export default function team() {
  return (
    <div className='team'>
    <h1>
        mini project(EXPERT-SYSTEM) <br/>
        <span>Realised By</span>
    </h1>
    <div className='members'>
        <div>
            <img src="" alt="" />
        </div>
        <div className='information'>
          <div class="box">
              <img src={image} alt=""/>
              <div className="content">
                <h3>HAMLAOUI WAIL</h3>

                <div class="personal-info">
                  <div class="icon-container">
                    <i class="fas fa-envelope"></i>
                  </div>
                  <div class="info-container">
                    <p>w_hamlaoui@estin.dz</p>
                  </div>
                </div>

                <div class="personal-info">
                  <div class="icon-container">
                    <i class="fas fa-phone"></i>
                  </div>
                  <div class="info-container">
                    <p>06 67 80 99 90</p>
                  </div>
                </div>
              </div>
          </div>

          <div class="box">
            <img src={image} alt=""/>
            <div className="content">
              <h3>SOUDA ACHREF</h3>

                <div class="personal-info">
                  <div class="icon-container">
                    <i class="fas fa-envelope"></i>
                  </div>
                  <div class="info-container">
                    <p>a_souda@estin.dz</p>
                  </div>
                </div>

                <div class="personal-info">
                  <div class="icon-container">
                    <i class="fas fa-phone"></i>
                  </div>
                  <div class="info-container">
                    <p> 06 60 03 17 46 </p>
                  </div>
                </div>
              
            </div>
          </div>
        </div>
    </div>
    </div>
  )
}
