from flask import Flask, render_template,request
from Bio import pairwise2
from Bio.Seq import Seq

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pairwise.html')

@app.route('/pairalignment')
def pairalignment():
    x = request.args['seq1']
    y = request.args['seq2']
    match=int(request.args['match'])
    mismatch=int(request.args['mismatch'])
    gap=int(request.args['gap'])
    alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
    from Bio.pairwise2 import format_alignment
    g = format_alignment(*alignments[0])

    return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***   
#     ***
#     from flask import Flask, render_template,request
# from Bio import pairwise2
# from Bio.Seq import Seq

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('pairwise.html')

# @app.route('/pairalignment')
# def pairalignment():
#     x = request.args['seq1']
#     y = request.args['seq2']
#     match=int(request.args['match'])
#     mismatch=int(request.args['mismatch'])
#     gap=int(request.args['gap'])
#     alignments = pairwise2.align.globalms(x, y,match,mismatch,gap,0)
#     from Bio.pairwise2 import format_alignment
#     g = format_alignment(*alignments[0])

#     return render_template('result.html',seq1= request.args['seq1'],seq2=request.args['seq2'],match=request.args['match'],mismatch=request.args['mismatch'],gap=request.args['gap'],SEQ3=g)
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
#     ***
