import ImageList from "@material-ui/core/ImageList";
import React from "react";
import ImageListItem from "@material-ui/core/ImageListItem";
import Card from "@material-ui/core/Card";
import {video} from "../data/video";
import PlayerModal from "./PlayerModal";
import Paper from "@material-ui/core/Paper";
import ImageListItemBar from "@material-ui/core/ImageListItemBar";
import IconButton from "@material-ui/core/IconButton";
import InfoIcon from '@mui/icons-material/Info';

export default function VideoGallery() {


    return (
        <ImageList sx={{width: 350, height: 250}} cols={3} rowHeight={250}>
            {video.map((item) => (



                        <PlayerModal
                            key={item.url}
                            url={item.url}
                            name={item.name}
                        />






            ))}


        </ImageList>
    )

}