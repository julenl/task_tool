
% if len(tasks) > 0:
%   fields = next(iter(tasks)).keys()

<table class="table">
  <thead class="thead-dark">
    <tr>
    % for f in fields:
      <th> {{f}} </th>
    % end
    </tr>
  </thead>

  <tbody>
    % for item in tasks:
    <tr>
      % for f in fields:
        <td>{{str(item[f])}}</td>
      % end
        <td>
          <a href="form?name={{str(item['name'])}}"><span class="glyphicon glyphicon-pencil"></span></a>
        </td>
        <td>
          <a href="delete?name={{str(item['name'])}}"><span class="glyphicon glyphicon-trash"></span></a>
        </td>
    </tr>
    % end
  </tbody>

</table>
