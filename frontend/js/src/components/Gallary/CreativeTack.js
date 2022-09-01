import Box from "@mui/material/Box";
import React from "react";
import Card from "@mui/material/Card";
import BrushIcon from '@mui/icons-material/Brush';
import AssignmentIcon from '@mui/icons-material/Assignment';
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Typography from "@mui/material/Typography";
import {Paper} from "@mui/material";

export default function CreativeTack(props) {
    if (props.data.length !== 0) {
        return (
            <Card sx={{
                margin: '25px',
                padding: ['5px','10px'],
                boxShadow: 0,
                border: 2,
                borderColor: '#dad2d2',

            }}

            >


                <Tooltip title="Творческое задание">
                    <IconButton>
                        <AssignmentIcon sx={{
                            fontSize: '2rem',
                            color: 'rgb(128,110,110)',
                            padding: '2px'
                        }}/>
                    </IconButton>
                </Tooltip>

                <Paper
                     // overflow={'auto'}
                     // maxHeight={600}
                     dangerouslySetInnerHTML={{__html: props.data}}
                     scroll={'body'}
                     sx={{
                         boxShadow: 0,
                         maxHeight:600,
                         overflow:'auto',
                         padding:['5px','25px'],
                     }}

                >


            </Paper>
            </Card>
        )
    }

}