import Card from "@mui/material/Card";
import {CardMedia, Chip, ImageListItemBar, Paper} from "@mui/material";
import Box from "@mui/material/Box";

import React from "react";
import {getFormattedDate} from "../utils/utils";
import ImageListItem from "@mui/material/ImageListItem";
import EventNoteIcon from "@mui/icons-material/EventNote";

import IconButton from "@mui/material/IconButton";
import {host} from "../utils/consts";
import {Link} from "react-router-dom"
import Tooltip from "@mui/material/Tooltip";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";


function CardExposition(props) {
    // const urlExposition = `${host}/exposition/${props.data.id}/`
    const [isFetching, setIsFetching] = React.useState(true)
    let optionsDate = {
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',

    };
    return (

        <ImageListItem >

            <Paper>
                <Link to={`/exposition/${props.data.id}`}>
                    <img
                        src={props.data.poster['thumb']}
                        alt={props.data.title}
                        loading="lazy"
                        onLoad={()=>{setIsFetching(false)}}
                    />
                </Link>

                {isFetching?'':
                <ImageListItemBar
                    sx={{
                        backgroundColor: "rgba(138, 119, 119, 0.89)"
                    }}
                    title={
                        props.data['virtual'] ? 'Виртуальная выставка' :
                            getFormattedDate(props.data['start_date'], optionsDate) + ' - ' +
                            getFormattedDate(props.data['end_date'], optionsDate)
                    }
                    actionIcon={

                        <IconButton>
                            <EventNoteIcon sx={{
                                color: "#fff",
                                p: '5px'
                            }}/>
                        </IconButton>

                    }/>
}

            </Paper>

        </ImageListItem>



    )
}


export default CardExposition