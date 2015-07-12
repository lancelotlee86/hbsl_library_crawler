{
    'student_number' : '201315414',
    'record' : [
        {
            'date' : '2015/06/04',
            'books_count': 2,
            'books' : [
                {
                    'title' : '离散数学导学',
                    'lend_date': '2015/1/9',
                    'return_deadline': '2015/8/5',
                    'renew_times': '0',
                    'located': '新校区流通1库（新校区一楼）'
                },
                {
                    'title' : '数据结构与算法分析',
                    'lend_date': '2015/1/20',
                    'return_deadline': '2015/4/28',
                    'renew_times': '1',
                    'located': '新校区流通1库（新校区一楼）'
                }
            ]
        },
        {
            'date': '2015/06/05',
            'books_count': 1,
            'books': [
                {
                    'title' : '离散数学导学',
                    'lend_date': '2015/1/9',
                    'return_deadline': '2015/8/5',
                    'renew_times': '0',
                    'located': '新校区流通1库（新校区一楼）'
                }
            ]
        }
    ]
}

# 更新一条记录，每天更新一次，更新到特定的人
db.record.update(
    {'student_number': '201315414'},
    { '$addToSet': {
        'record': {
            'date': '2015/06/06',
            'books_count': 1,
            'books': [
                {
                    'title': '算法I-IV(C++实现)',
                    'lend_date': '2015/3/15',
                    'return_deadline': '2015/5/14',
                    'renew_times': '0',
                    'located': '新校区流通1库（新 校区一楼）'
                }
            ]
        }}
    }
)

{'_id': ObjectId('557aa6aa2f8f461d60204d68'),
 'record': [
    {
        'books': [{'lend_date': '2015/1/9',
     'located': '新校区流通1库（新校区一楼）',
     'renew_times': '0',
     'return_deadline': '2015/8/5',
     'title': '离散数学导学'},
    {'lend_date': '2015/1/20',
     'located': '新校区流通1库（新校区一楼）',
     'renew_times': '1',
     'return_deadline': '2015/4/28',
     'title': '数据结构与算法分析'}],
   'books_count': 2,
   'date': '2015/06/04'},
  {'books': [{'lend_date': '2015/1/9',
     'located': '新校区流通1库（新校区一楼）',
     'renew_times': '0',
     'return_deadline': '2015/8/5',
     'title': '离散数学导学'}],
   'books_count': 1,
   'date': '2015/06/05'},
  {'books': [{'lend_date': '2015/3/15',
     'located': '新校区流通1库（新 校区一楼）',
     'renew_times': '0',
     'return_deadline': '2015/5/14',
     'title': '算法I-IV(C++实现)'}],
   'books_count': 1,
   'date': '2015/06/06'}],
 'student_number': '201315414'}
