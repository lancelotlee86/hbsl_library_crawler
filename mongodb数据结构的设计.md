db: ncwu_library
collection: library_record
one document:
{
    '_id' : ObjectId("56f4ef948743d414cad75cf8"),
    'student_number' : '201315414',
    'password' : '201400101',
    "school_id" : "967",
    'result_url' : 'http://202.196.146.145:8080/sms/opac/user/lendStatus.action?sn=A03B7B762168599F9029989AAF686F30C62FB4F1908FBE53A3B34BFEA74E47B5A11F5D2E1A1BF78F20DD4DECCFDE3B0EEFC215810305DD9CE5CDB79E95E8912E5CAFA57D0C7549BA&xc=5',
    'record' : [
        {
            "date" : ISODate("2016-03-25T18:53:00.439Z"),
            'books_count': 2,
            'books' : [
                {
                    'title' : '离散数学导学',
                    'lend_date' : ISODate("2016-03-02T00:00:00Z"),
					"return_deadline" : ISODate("2016-05-02T00:00:00Z"),
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
                    'located': '新校区流通1库（新校区一楼）'
                }
            ]
        }}
    }
)






# 一个例子
{
    '_id': ObjectId('557aa6aa2f8f461d60204d68'),
    'student_number': '201315414',
    'record': 
        [
            {
                'books_count': 2,
                'date': '2015/06/04',
                'books': 
                    [
                        {
                            'lend_date': '2015/1/9',
                             'located': '新校区流通1库（新校区一楼）',
                             'renew_times': '0',
                             'return_deadline': '2015/8/5',
                             'title': '离散数学导学'
                        },
                        {
                            'lend_date': '2015/1/20',
                            'located': '新校区流通1库（新校区一楼）',
                            'renew_times': '1',
                            'return_deadline': '2015/4/28',
                            'title': '数据结构与算法分析'
                        }
                    ]
            },
            {
                'books_count': 1,
                'date': '2015/06/05',
                'books': 
                    [
                        {
                            'lend_date': '2015/1/9',
                            'located': '新校区流通1库（新校区一楼）',
                            'renew_times': '0',
                            'return_deadline': '2015/8/5',
                            'title': '离散数学导学'
                        }
                    ]
            },
            {
                'books_count': 1,
                'date': '2015/06/06'，
                'books': 
                    [
                        {
                            'lend_date': '2015/3/15',
                            'located': '新校区流通1库（新 校区一楼）',
                            'renew_times': '0',
                            'return_deadline': '2015/5/14',
                            'title': '算法I-IV(C++实现)'
                        }
                    ]
            }
        ]
}
