/**
 * Created by vlad on 22.11.16.
 */
var React = require('react');
var Link = require('react-router').Link;
import { Card, CardHeader, CardActions, RaisedButton, Paper } from 'material-ui';
import { ActionCheckCircle, ActionCached, AlertError, ActionDelete, ActionList } from 'material-ui/svg-icons';
import { get_task_list } from '../../api/task'
import { red500, yellow500, green500 } from 'material-ui/styles/colors';


class TasksList extends React.Component{
    constructor(props) {
        super(props);
        this.state = {tasks_list: []};
    }

    componentDidMount() {
        this.update_task_list();
        this.timerID = setInterval(
            () => this.update_task_list(),
            5000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    update_task_list(){
        get_task_list().then(data => {
            this.setState({
                tasks_list: data
            });
        });
    }

    render(){
        let panel_list = '';
        if(this.state.tasks_list){
            panel_list = this.state.tasks_list.map(function(task) {
                let state,
                    icon,
                    link = <Link to={'/tasks/' + task.id} />,
                    style = {
                        whiteSpace: 'nowrap',
                        overflow: 'hidden',
                        textOverflow: 'ellipsis'
                    },
                    header = '#'+task.id.toString()+' '+(task.title ? task.title : JSON.parse(task.request).method.split('.').pop());
                switch(task.state){
                    case 0:
                    case 1:
                        icon = <ActionCached color={yellow500}/>;
                        state = 'Выполняется';
                        break;
                    case 2:
                        icon = <ActionCheckCircle color={green500}/>;
                        state = 'Выполненно';
                        break;
                    default:
                        icon = <AlertError color={red500}/>;
                        state = 'Ошибка';
                }
                return (
                    <Card style={{marginBottom: 5}}>
                        <CardHeader
                            title={header}
                            subtitle={state}
                            avatar={icon}
                        />
                        {task.state == 2?
                        <CardActions>
                            <RaisedButton
                                primary={true}
                                containerElement={link}
                                label="Посмотреть результат" />
                        </CardActions>:
                            <CardActions>
                                <RaisedButton
                                    disabled={true}
                                    label="Посмотреть результат" />
                            </CardActions>
                        }
                    </Card>
                );
            })
        }
        return(
            <div> {panel_list} </div>
        );
    }
}

export default TasksList
