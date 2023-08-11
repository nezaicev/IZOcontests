import {CardMedia, Chip, ImageListItemBar, Paper} from "@mui/material";
import React from "react";

import ImageListItem from "@mui/material/ImageListItem";

import ArticleIcon from '@mui/icons-material/Article';
import IconButton from "@mui/material/IconButton";
import {Link} from "react-router-dom"
import Box from "@mui/material/Box";

function CardPublication(props) {
    const [isFetching, setIsFetching] = React.useState(true)
    return (

        <ImageListItem>

            <Box sx={{marginTop:'10px'}}>
                <a href={props.link}>
                    <img
                        src={props.poster['thumb']}
                        alt={props.title}
                        loading="lazy"
                        onLoad={()=>{setIsFetching(false)}}
                    />


                    {isFetching?'':<ImageListItemBar
                    sx={{
                        backgroundColor: "rgba(138, 119, 119, 0.89)",
                        fontSize: '10px',
                        '& .MuiImageListItemBar-title': {
                            whiteSpace: "normal",
                        },
                    }}
                    title={
                        props.title
                    }
                    actionIcon={

                        <IconButton>
                            <ArticleIcon sx={{
                                color: "#fff",
                                p: '5px'
                            }}/>
                        </IconButton>

                    }
                /> }
                    </a>
            </Box>

        </ImageListItem>


    )
}


export default CardPublication