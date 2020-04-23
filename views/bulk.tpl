<!DOCTYPE html>
<head lang="en">
    <title>Bulk Objects</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Use bootstrap instead of own CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <style>
    </style>
</head>
<body>

%include('navigation')
%setdefault('content','')

% if defined('db_empty'):
%  include('test_tasks')
% elif defined('tasks'):
%  include('task_table', tasks=tasks)
% elif defined('stats'):
%   for k, v in stats.items():
    <div> <img src="{{v}}"></div>
%   end
% else:
{{!content}}
% end


</body>
</html>

