import VerticalTabs from "../VerticalTabs";
import HorizontalTabs from "../HorizontalTabs";
import React, {useEffect, useState} from "react";
import {Box} from "@mui/material";
import dataFetch from "../../utils/dataFetch";
import {ExpandMoreCollapse} from "./ItemVisibleVP";
import VisibleBoxVP from "./VisibleBoxVP";


export default function GalleryVP(props) {
    const [dataVerticalTabs, setDataVerticalTabs] = React.useState([])
    const [valueVerticalTabs, setValueVerticalTabs] = React.useState('')
    const [dataHorizontalTabs, setDataHorizontalTabs] = React.useState([])
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [params, setParams] = React.useState({contest_name: props.contestName})
    const [page, setPage] = useState(1)


    useEffect(() => {
        dataFetch(props.urlVerticalTabs, params, (data) => {
            setDataVerticalTabs(data, [setValueVerticalTabs(0)]);
        })
    }, [])

    useEffect(() => {
        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        if (params['year_contest']){
        dataFetch(props.urlHorizontalTabs, params, (data) => {
            setDataHorizontalTabs(data, [setValueHorizontalTabs(0)])
        })}
    }, [valueVerticalTabs])


    return (<React.Fragment>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <HorizontalTabs contestName={props.contestName}
                                data={dataHorizontalTabs}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue), [setPage(1)]))}
                                valueVerticalTabs={valueVerticalTabs}
                />

                <VerticalTabs contestName={props.contestName}
                              data={dataVerticalTabs}
                              setValueVerticalTabs={(newValue) => (setValueVerticalTabs(newValue, [setPage(1)]))}

                />
            </Box>
            <Box sx={{}}>

                <VisibleBoxVP
                    url={props.urlContent}
                    contestName={props.contestName}
                    year={dataVerticalTabs[valueVerticalTabs]}
                    nomination={dataHorizontalTabs[valueHorizontalTabs]}
                    theme={null}
                    page={page}
                    setPage={(newValue) => {
                        setPage(newValue)
                    }}
                />

            </Box>
        </React.Fragment>
    )
}