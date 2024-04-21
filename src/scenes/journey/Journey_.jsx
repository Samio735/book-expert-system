import React from "react";
import { useNavigate } from "react-router-dom";
import "./journey.css";
import Search from "../../componant/Search";
import PersonalInfo from "./../../componant/PersonalInfo";
import Button from "../../componant/Button";

const BookList = [
  {
    image: "",
    title: "Zero to one",
  },
  {
    image: "",
    title: "The lean startup",
  },
  {
    image: "",
    title: "Rich dad poor dad",
  },
  {
    image: "",
    title: "The 4 hour work week",
  },
  {
    image: "",
    title: "The 7 habits of highly effective people",
  },
  {
    image: "",
    title: "The 48 laws of power",
  },
];

export default function Journey_() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/details", { state: { content: BookList } });
  };
  const handleChange = () => {};

  return (
    <div className="JorneyContant">
      <h1 className="mt-6">
        We think that these books will be interesting to you
      </h1>

      <div className="contantSearch">
        {BookList.map((item, index) => (
          <div className="BookSResultat" key={index}>
            <div
              className="imageC"
              style={{ padding: "20px", width: "200px" }}
              onClick={handleClick}
            >
              {" "}
              <div
                className="title"
                style={{ width: "160px", fontSize: "25px" }}
              >
                {item.title}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* <div className="contantSearch">
        <div className='BookSResultat'>
          <div className="imageC">

          </div>
          <div className="title">
            Fire and Shitty crap in
            asd teq
          </div>
        </div>

        <div className='BookSResultat'>
          <div className="imageC">

          </div>
          <div className="title">
            Fire and Shitty crap in
            asd teq
          </div>
        </div>

        <div className='BookSResultat'>
          <div className="imageC">

          </div>
          <div className="title">
            Fire and Shitty crap in
            asd teq
          </div>
        </div>
        
        <div className='BookSResultat'>
          <div className="imageC">

          </div>
          <div className="title">
            Fire and Shitty crap in
            asd teq
          </div>
        </div>
      </div> */}
    </div>
  );
}
