from task1_main import main
from nose.tools import *
import nose
import pickle

images_folder = "test_images/"

# output files for 8 boards
BD_filename = images_folder+"BD_8.p"
DO_filename = images_folder+"DO_8.p"   

f = open(BD_filename, 'r')
BD_8 = pickle.load(f)
f.close()

f = open(DO_filename, 'r')
DO_8 = pickle.load(f)
f.close()

board = images_folder+"board_8.jpg"

container_1 = images_folder+"container_1.jpg"
container_2 = images_folder+"container_2.jpg"
container_3 = images_folder+"container_3.jpg"
container_4 = images_folder+"container_4.jpg"
container_5 = images_folder+"container_5.jpg"

container = [container_1,container_2,container_3,container_4,container_5]

def test_main_board_shapes():
    board_shapes, output_list = main(board, container_1)
    assert_equals(board_shapes, BD_8)

def main_output_list(board, container, i):
    board_shapes, output_list = main(board, container)
    try:
        assert_items_equal(output_list,DO_8[i])
    except AssertionError,e:
        raise(AssertionError( "List Must be Sorted %s",e))    

def test_final_output_list():
    for i in range(0,5):
        yield main_output_list, board, container[i], i


def main_sorted_output_list(board, container, i):
    board_shapes, output_list = main(board, container)
    try:
        assert_equals(output_list,DO_8[i])
    except AssertionError,e:
        raise(AssertionError( "List Must be Sorted %s",e))    

def test_final_output_list_if_sorted():
    for i in range(0,5):
        yield main_sorted_output_list, board, container[i], i

if __name__ == '__main__':
    import nose
    # nose.run(defaultTest=__name__)
    nose.run(argv=["", "test_task1_main", "--with-doctest","--verbosity=3"])
