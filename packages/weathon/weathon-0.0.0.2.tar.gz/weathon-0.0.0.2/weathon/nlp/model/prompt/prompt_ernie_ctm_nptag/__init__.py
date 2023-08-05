from ark_nlp.dataset import PromptDataset as Dataset
from ark_nlp.dataset import PromptDataset as PromptErnieCtmNptagDataset

from ark_nlp.model.prompt.prompt_ernie_ctm_nptag.prompt_ernie_ctm_nptag_tokenizer import PromptErnieCtmNptagTokenizer as Tokenizer
from ark_nlp.model.prompt.prompt_ernie_ctm_nptag.prompt_ernie_ctm_nptag_tokenizer import PromptErnieCtmNptagTokenizer as PromptErnieCtmNptagTokenizer
from ark_nlp.model.prompt.prompt_ernie_ctm_nptag.prompt_ernie_ctm_nptag_tokenizer import PromptErnieCtmNptagTokenizer

from ark_nlp.nn import BertConfig as PromptErnieCtmNptagConfig
from ark_nlp.nn import BertConfig as ModuleConfig

from ark_nlp.model.prompt.prompt_ernie_ctm_nptag.prompt_ernie_ctm_nptag import PromptErnieCtmNptag
from ark_nlp.model.prompt.prompt_ernie_ctm_nptag.prompt_ernie_ctm_nptag import PromptErnieCtmNptag as Module

from ark_nlp.factory.optimizer import get_default_bert_optimizer as get_default_model_optimizer
from ark_nlp.factory.optimizer import get_default_bert_optimizer as get_default_prompt_ernie_ctm_nptag_optimizer

from ark_nlp.factory.task import PromptMLMTask as Task
from ark_nlp.factory.task import PromptMLMTask as PromptErnieCtmNptagTask

from ark_nlp.factory.predictor import PromptMLMPredictor as Predictor
from ark_nlp.factory.predictor import PromptMLMPredictor as PromptErnieCtmNptagPredictor
