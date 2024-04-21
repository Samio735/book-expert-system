import React from 'react'
import ContReading from "../scenes/images/icons8-shift-up-96 1.png"
import "./button.css"

export default function Button(props) {
    const propsValue = props.props
  return (
    <div className="btn-cont">
        <a>{propsValue}</a>
        <img src={ContReading} alt="" />
    </div>
  )
}
