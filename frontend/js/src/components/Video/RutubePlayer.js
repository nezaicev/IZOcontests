import * as React from "react";

function RutubePlayer(props) {


    return (
        <div className="react-player">
        <iframe width="720" height="405"
                title={props.title}
                src={props.url} frameBorder="0"
                allow="clipboard-write; autoplay" webkitAllowFullScreen mozallowfullscreen
                allowFullScreen></iframe>
            </div>
    )


}


export {RutubePlayer}