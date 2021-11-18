from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.responses import FileResponse
################################################################################
import uvicorn
import subprocess
from FSM_V1 import States, Transitions, FSM
from schemas.schemas import BaseInput
from utils.utils import Formater
################################################################################

# APP CONFIG
app = FastAPI(
    title="APP-TWO-API",
    version="1.0.5",
    contact={
        "name": "Nícolas Marques de Moura Barbosa",
        "url": "https://www.linkedin.com/in/nicolasmmb/",
        "email": "nicolas.mmb@hotmail.com",
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

StatesSTD = States
TransitionsSTD = Transitions


@app.post("/", status_code=status.HTTP_200_OK)
def set_the_state_and_transitions_of_FSM(modelFSM: BaseInput):
    if not modelFSM.state:
        return {
            "EstadosPossiveis": [States.ACORDADO, States.DESCANSANDO, States.DORMINDO, States.TRABALHANDO],
        }
    if not modelFSM.transitions:
        return {
            "TransicoesPossiveis": [Transitions.TR_08_00, Transitions.TR_12_00, Transitions.TR_13_00, Transitions.TR_18_00, Transitions.TR_22_00],
        }

    fsm = FSM(modelFSM.state, Formater.format_input_to_list(modelFSM.transitions))

    return {
        "EstadoAtual": fsm.get_state(),
    }


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
