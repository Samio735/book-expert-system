import React,{ useState }   from 'react'
import image from "../images/icons8-hourglass-64 1.png"
import image1 from "../images/icons8-cash-80 1.png"
import "./Form.css"

export default function Form() {

    const [checkboxes, setCheckboxes] = useState({
        checkbox1: false,
        checkbox2: false,
        checkbox3: false,
        checkbox4: false,
      });
    
      const handleCheckboxChange = (event) => {
        const { name, checked } = event.target;
        setCheckboxes({
          ...checkboxes,
          [name]: checked,
        });
      };

  return (
    <div className='formI'>
        
        <div className='form'>
            <h1>
            Let’s Start Customizing Your Journey 
            </h1>
            <p>Help Us customize your journey by answering few consize questions</p>
            <h1 className="Qst">
              What are your Goals ? 
            </h1>

            <div className="Goals">
                <div className="container">
                <div className="list">

                   <div className="form-element">
                        <input type="checkbox" name="platForm" value="" id="i" />
                        <label htmlFor="i">
                        
                            <div className="title">
                                Win at work
                            </div>
                            <div className="icon">
                                <img src={image} alt="" />
                            </div>
                        </label>
                    </div>    

                    <div className="form-element">
                    <input type="checkbox" name="platForm" value="instagram" id="instagram" />
                    <label htmlFor="instagram">
                        
                        <div className="title">
                         Have More Money
                        </div>
                        <div className="icon">
                            <img src={image1} alt="" />
                        </div>
                    </label>
                    </div>

                    <div className="form-element">
                        <input type="checkbox" name="platForm" value="" id="i22" />
                        <label htmlFor="i22">
                        
                            <div className="title">
                                Be Productive
                            </div>
                            <div className="icon">
                                <img src={image} alt="" />
                            </div>
                        </label>
                    </div>                    

                    <div className="form-element">
                    <input type="checkbox" name="platForm" value="slack" id="slack"/>
                    <label htmlFor="slack">
                       
                        <div className="title">
                        Build strong family
                        </div>
                        <div className="icon">
                            <img src={image} alt="" />
                        </div>
                    </label>
                    </div>
                    <div className="form-element">
                    <input type="checkbox" name="platForm" value="pinterest" id="pinterest"/>
                    <label htmlFor="pinterest">
                       
                        <div className="title">
                        have a healthy body
                        </div>
                        <div className="icon">
                            <img src={image} alt="" />
                        </div>
                    </label>
                    </div>
                    <div className="form-element">
                    <input type="checkbox" name="platForm" value="dribbble" id="dribbble"/>
                    <label htmlFor="dribbble">
                       
                        <div className="title">
                         Improve Discipline
                        </div>
                        <div className="icon">
                            <img src={image} alt="" />
                        </div>
                    </label>
                    </div>
                    <div className="form-element">
                        <input type="checkbox" name="platForm" value="" id="i3" />
                        <label htmlFor="i3">
                        
                            <div className="title">
                                Be Happy
                            </div>
                            <div className="icon">
                                <img src={image} alt="" />
                            </div>
                        </label>
                    </div>    

                    <div className="form-element">
                        <input type="checkbox" name="platForm" value="" id="i1" />
                        <label htmlFor="i1">
                        
                            <div className="title">
                                Improve social life
                            </div>
                            <div className="icon">
                                <img src={image} alt="" />
                            </div>
                        </label>
                    </div>    


                    <div className="form-element">
                        <input type="checkbox" name="platForm" value="" id="i2" />
                        <label htmlFor="i2">
                        
                            <div className="title">
                                Learn programming
                            </div>
                            <div className="icon">
                                <img src={image} alt="" />
                            </div>
                        </label>
                    </div>    

                </div>
               </div>
            </div>

            <button className='btn-next mt-6'>
                <a href='/Journey'>Continue</a>
            </button>
        </div>
    </div>
  )
}