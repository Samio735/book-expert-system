import React from "react";
import PersonalInfo from "../../componant/PersonalInfo";
import Search from "../../componant/Search";
import "./BookSummary.css";

export default function BookSummary() {
  return (
    <div className="BookSummary">
      <div className="pageElement">
        <div className="imageCO"></div>
        <div className="EContent">
          <h1>Can’t hurt me son</h1>
          <h2>David Goggins</h2>
          <p>
            Get ready to dominate your inner voices and learn how to stay hard
            son . Get ready to dominate your inner voices and learn how to stay
            hard son .
          </p>
        </div>
      </div>
      <div className="KeyPoints">
        <div className="KeyPoints_">
          <h1>Key Points</h1>
          <hr className="line2" />
          <div>
            <span>1.</span>
            <p>Keep Yourself Inline jonga shis</p> <br />
            <span>2.</span>
            <p>Practice till you piss blood</p>
            <br />
            <span>3.</span>
            <p>Wake up everyday thankfull and ready to destroy yourself</p>
            <br />
            <span>4.</span>
            <p>Kill all your cats and chickens</p>
            <br />
            <span>5.</span>
            <p>Don’t forget to make sha5shou5a when you hunt a deer</p> <br />
          </div>
        </div>

        <br />
        <br />
        <h1>Summary</h1>
        <hr className="line2" />

        <div className="Summary">
          <div>
            <span>1.</span>
            <h2>Keep Yourself Inline jonga shis</h2>
            <div>
              <p className="textS">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
                risus tellus, finibus sed eleifend eget, dictum et erat. Quisque
                vel accumsan turpis. Integer quis eros turpis. Etiam vestibulum
                lorem eget velit faucibus, dapibus efficitur nibh maximus. Sed
                finibus, dolor in sollicitudin laoreet, nunc diam faucibus
                metus, at egestas risus nunc ac sapien. Donec sodales vehicula
                malesuada. Vivamus eget dignissim ante. Nunc eget diam
                ultricies, lobortis massa et, sodales ipsum. Integer dictum nisl
                nec dui posuere, ut condimentum elit viverra. Nam blandit, risus
                vel tristique interdum, dolor augue dapibus magna, hendrerit
                commodo risus nulla ultricies nibh. Fusce eleifend, velit at
                dignissim faucibus, nunc ex rhoncus diam, viverra consectetur
                nisl ligula sit amet felis. Nunc fringilla nisl lectus, nec
                vestibulum sapien molestie.
              </p>
            </div>
          </div>

          <div>
            <span>2.</span>
            <h2>Keep Yourself Inline jonga shis</h2>
            <div>
              <p className="textS">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
                risus tellus, finibus sed eleifend eget, dictum et erat. Quisque
                vel accumsan turpis. Integer quis eros turpis. Etiam vestibulum
                lorem eget velit faucibus, dapibus efficitur nibh maximus. Sed
                finibus, dolor in sollicitudin laoreet, nunc diam faucibus
                metus, at egestas risus nunc ac sapien. Donec sodales vehicula
                malesuada. Vivamus eget dignissim ante. Nunc eget diam
                ultricies, lobortis massa et, sodales ipsum. Integer dictum nisl
                nec dui posuere, ut condimentum elit viverra. Nam blandit, risus
                vel tristique interdum, dolor augue dapibus magna, hendrerit
                commodo risus nulla ultricies nibh. Fusce eleifend, velit at
                dignissim faucibus, nunc ex rhoncus diam, viverra consectetur
                nisl ligula sit amet felis. Nunc fringilla nisl lectus, nec
                vestibulum sapien molestie.
              </p>
            </div>
          </div>
        </div>

        <hr className="line___" />
      </div>
    </div>
  );
}
