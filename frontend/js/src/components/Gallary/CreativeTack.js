import Box from "@mui/material/Box";
import React from "react";
import Card from "@mui/material/Card";
import BrushIcon from '@mui/icons-material/Brush';
import AssignmentIcon from '@mui/icons-material/Assignment';
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Typography from "@mui/material/Typography";

export default function CreativeTack(props) {
    if (props.data.length !== 0) {
        return (
            <Card sx={{
                    padding: '20px',
                    boxShadow: 0,
                    border: 2,
                    borderColor: '#dad2d2'
                }}>


                    <Tooltip title="Творческое задание" sx={{marginLeft:'-15px', marginTop:'-15px'}}>
                        <IconButton>
                            <AssignmentIcon sx={{
                                fontSize: '2rem',
                                color: 'rgb(128,110,110)',
                                padding: '2px'
                            }}/>
                        </IconButton>
                    </Tooltip>
                 <Box component='div'
                      dangerouslySetInnerHTML={{__html: props.data}}>

                </Box>
            </Card>
        )
    }

}