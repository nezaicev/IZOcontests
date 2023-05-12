import Card from "@mui/material/Card";
import {CardMedia, Chip, ImageListItemBar} from "@mui/material";
import Box from "@mui/material/Box";

import React from "react";
import {getFormattedDate} from "../utils/utils";
import ImageListItem from "@mui/material/ImageListItem";
import EventNoteIcon from "@mui/icons-material/EventNote";

import IconButton from "@mui/material/IconButton";
import {host} from "../utils/consts";
import {Link} from "react-router-dom"




function CardExposition(props) {
    const urlExposition=`${host}/exposition/${props.data.id}/`
    let optionsDate = {
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',

    };
    return (
        <ImageListItem
            sx={{marginTop: '15px', margin:'10'}}

        >
            <Card sx={{border: 7, borderColor: '#fff', boxShadow: 0}}>
                <Link to={`/exposition/${props.data.id}`}>
                    <img
                        src={props.data.poster['thumb']}
                        alt={props.data.title}
                        loading="lazy"
                    />
                </Link>
                { props.data.poster['thumb'] ? <ImageListItemBar
                    sx={{
                        backgroundColor: "rgba(138, 119, 119, 0.89)"
                    }}
                    title={
                        props.data['virtual']? 'Виртуальная выставка':
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

                    }/>:''}

            </Card>

        </ImageListItem>

    )
}


export default CardExposition