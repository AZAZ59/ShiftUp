/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';


class GetGroupsPosts extends React.Component{
    method_name = 'Collector.Groups.get_groups_posts';
    default_state = {group_ids: '', count: '', all: true};

    constructor(props) {
        super(props);
        this.state = this.default_state;
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);
    }

    handleChange(event) {
        this.setState({group_ids: event.target.value});
    }

    handleCountChange(event) {
        if(event.target.value.length > 0){
            this.setState({all: !this.state.all});
        }
        this.setState({count: event.target.value});
    }


    handleSubmit(event) {
        var group_ids = this.state.group_ids.split(',');
        if(this.state.group_ids.length == 0){
            alert('Error!')
        }
        else {
            if(this.state.all){
                send_task(this.method_name, {
                    'group_ids': group_ids
                });
            }
            else {
                send_task(this.method_name, {
                    'group_ids': group_ids,
                    'count': this.state.count
                });
            }
        }
        this.setState(this.default_state);
        event.preventDefault();
    }

    render(){
        return(
            <div class = 'content'>
                <div className="page-header">
                    <h1>Сбор постов групп</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите список сообществ через запятую:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.group_ids}
                            placeholder="coffman, club1, 2"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>Какое кол-во постов выгрузить:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.count}
                            placeholder="По-умолчанию все посты"
                            onChange={this.handleCountChange}
                        />
                    </FormGroup>
                    <Button type="submit">
                        Отправить
                    </Button>
                </form>
            </div>
        );
    }
};

export default GetGroupsPosts
