import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import {TextField} from "@mui/material";

function Comment(){
    return(
        <Box>
            <TextField id="author" label="Standard" variant="standard" />
            <TextField id="content" label="Standard" variant="standard" />
        </Box>
    )
}



export {Comment}
