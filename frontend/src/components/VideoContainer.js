import React from "react";
import BG_VID from "../utilis/Background_Video.mp4";
const VideoContainer = () => {
  return (
    <div>
      <div className="rounded-full">
      <video autoPlay loop muted>
        <source src={BG_VID} type="video/mp4" />
      </video>
    </div>
    </div>
  );
};

export default VideoContainer