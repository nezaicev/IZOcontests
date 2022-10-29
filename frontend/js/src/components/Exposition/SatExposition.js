import {
    Paper,
    Table, TableBody, TableCell,
    TableContainer,
    TableHead,
    TableRow
} from "@mui/material";
import React from "react";

function StatExposition(props) {

    return (
         <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Период проведения</TableCell>
            <TableCell align="right">Название</TableCell>
            <TableCell align="right">Место проведения</TableCell>
            <TableCell align="right">Участники (посетители)</TableCell>
            <TableCell align="right">Единицы экспонирования</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {props.data.map((item, index) => (
            <TableRow
              key={index}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="center">
                  {`${item.start_date} - ${item.end_date}`}
              </TableCell>
              <TableCell align="right">{item.title}</TableCell>
              <TableCell align="right">{item.address}</TableCell>
              <TableCell align="right">{item.count_participants}</TableCell>
              <TableCell align="right">{item.count_exp}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    )
}

export default StatExposition