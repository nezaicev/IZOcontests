import Box from "@mui/material/Box";
import {Grid} from "@mui/material";
import ItemBroadcast from "../Broadcast/ItemBroadcast";
import React from "react";
import VideoItem from "./VideoItem";


const GridVideoItems = (props) => {
    return (
        <Box>
            <Grid container spacing={2}
                  sx={{justifyContent: 'space-between'}}>
                {props.data.map((item, index) => (
                    item['link'] ?
                        <Grid item xs="auto" key={index}>
                            <VideoItem link={item['link']} title={item['title']} />
                        </Grid> : ''
                ))}

            </Grid>
        </Box>
    )
}


export {GridVideoItems}