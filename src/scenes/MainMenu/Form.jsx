import React from "react";
import intelligence from "../images/icons8-artificial-intelligence-100 (1) 1.png";
import table from "../images/line-icon-board-game-table-game-element-fun-activity-vector-illustration-tictactoe_721440-1914-removebg 3.png";
import personne from "../images/image 5.png";
import { Link } from "react-router-dom";

export default function Form() {
  return (
    <div className="flex h-screen">
      <div className="bg-gray-200 p-10 w-[70%]">
        <div className="flex justify-between">
          <div
            className="bg-[#0d3262] max-w-[40%] text-center py-4 border-white border-4 shadow-xl px-3"
            style={{
              border: "4px solid #F8F8F8",
              boxShadow:
                "4px 5px 20px rgba(0, 0, 0, 0.25), -4px -4px 4px rgba(0, 0, 0, 0.25)",
              borderRadius: "5px",
            }}
          >
            <Link to={"/Form_after"}>
              <img
                src={intelligence}
                alt="image1"
                className="w-48 h-48 m-auto"
              />
              <h1 className="text-2xl text-white">Expert System App</h1>
              <p className="text-sm text-justify text-slate-200">
                explaining a little bit explaining a little bit explaining a
                little bit explaining a little bit explaining a little bit
                explaining a little bit explaining a little bit explaining a
                little bit
              </p>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
