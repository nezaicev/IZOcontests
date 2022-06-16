import Typography from "@mui/material/Typography";
import Box from "@mui/material//Box";
import * as React from "react";


export default function FieldTitle(props) {
    if (props.content) {
        return (
            <Box>
                <Typography variant='subtitle2' component={'span'}>
                    {props.title}
                </Typography>
                <Typography variant='body2' component={'span'}>
                    {props.content}
                </Typography>
            </Box>

        )
    }
    else{
        return (<></>)
    }


}