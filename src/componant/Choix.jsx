import React, { useState,useEffect } from 'react'
import "./Choix.css"

export default function Choix() {

  // const radioButtons = document.querySelectorAll('input[name="channing-type"]');
  // let selectedValue;
  
  const [selectedOption, setSelectedOption] = useState("");

  useEffect(() => {
    const selected = document.querySelector('input[name="channing-type"]:checked');
    if (selected) {
      setSelectedOption(selected.id);
    }
  }, []);

  const handleChange = (e) => {
    setSelectedOption(e.target.id);
  };

  return (
    <>
       <div className="choix">
            <h1>Choose one type</h1>
            <h1 className="title-select">
                Select the Channing type :
            </h1>
            <div className="select-one">
                <label htmlFor="forward-channing">
                  <input type="radio" name="channing-type" id="forward-channing" onChange={handleChange}/>
                    Forward Channing 
                </label>

                <label htmlFor="backward-channing">
                  <input type="radio" name="channing-type" id="backward-channing" onChange={handleChange}/>
                    Backward Channing
                </label>
            </div>
            <p style={{color:"red",marginTop:"6px"}}>Selected Option: {selectedOption}</p>
            <button>
                Start
            </button>

        </div> 
    </>
  )
}
