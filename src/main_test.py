import main
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unittest import TestCase
import io
import sys
import mock

class TestMain(unittest.TestCase):

    def test_getOptions(self):
        salida_esperada = "\n    1. Load Options\n    2. Save Options\n    3. Add channel\n    4. Remove channel\n    5. Block channel\n    6. Calculate\n    7. Get Recomendations\n    0. Quit"
        salida_actual = main.getOptions()

        self.assertEqual(salida_actual, salida_esperada)

    @mock.patch('main.input')
    def test_getChannel(self, mock_open):
        salidas = ["Clase 1", "Ninja", "Ninga", "", " ", ".", "-12345667"]

        for r in range(len(salidas)):
            with self.subTest(r=r):
                capturedOutput = io.StringIO()                # Create StringIO object
                sys.stdout = capturedOutput                   #  and redirect stdout.
                obj = salidas[r]
                mock_open.return_value = obj

                salida_actual = main.getChannel()
                sys.stdout = sys.__stdout__                   # Reset redirect.
                printed = capturedOutput.getvalue()
                salida_esperada = obj

                self.assertEqual(salida_actual, salida_esperada)
                self.assertEqual(printed, "Enter name of channel: \n")
                mock_open.assert_called_with(">> ")

    @mock.patch('main.input')
    @mock.patch('main.getOptions')
    def test_takeAction(self, mock_input, mock_options):
        B = "Out of bounds!\n"
        N = "Please only numbers!\n"
        E = "\nTo many errors!\nHere are the options again:\n"

        entrada = [["4"], ["0"], ["7"], ["-1", "10", "8", "10000", "-10000", "5"], [" ", "one", "zero", "u8", "8o", "@", "", "2"]]
        salida_esperada = [4, 0, 7, 5, 2]
        print_esperado = [[], [], [], [B, B, B, E, B, B, E], [N, N, N, E, N, N, N, E, N]]

        for r in range(len(entrada)):
            mock_input.return_value = 4
            with self.subTest(r=r):
                ## FIXME: Not working
                #mock_input.side_effect = entrada[r]



                capturedOutput = io.StringIO()                # Create StringIO object
                sys.stdout = capturedOutput                   #  and redirect stdout.

                salida_actual = main.takeAction()

                sys.stdout = sys.__stdout__                   # Reset redirect.
                printed = capturedOutput.getvalue()

                print_esperado_completo = ""
                called_options = 0
                pr_esperado = print_esperado[r]
                for i in pr_esperado:
                    if i is E:
                        called_options += 1
                    print_esperado_completo += i

                self.assertEqual(salida_actual, salida_esperada[r])
                self.assertEqual(printed, print_esperado_completo)
                self.assertEqual(mock_options.call_count, called_options)
                self.assertEqual(mock_input.call_count, len(entrada[r]))



    def test_doAction(self):
        pass

    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()
